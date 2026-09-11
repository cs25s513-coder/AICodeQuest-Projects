import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";
import { EffectComposer } from "three/examples/jsm/postprocessing/EffectComposer.js";
import { RenderPass } from "three/examples/jsm/postprocessing/RenderPass.js";
import { ShaderPass } from "three/examples/jsm/postprocessing/ShaderPass.js";
import { UnrealBloomPass } from "three/examples/jsm/postprocessing/UnrealBloomPass.js";

import {
  diskFragmentShader,
  diskVertexShader,
  glowFragmentShader,
  glowVertexShader,
  LensingShader,
} from "./shaders.js";

const HORIZON_RADIUS = 3;

export function initBlackHoleScene(canvas) {
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const motionScale = prefersReducedMotion ? 0.15 : 1;

  const scene = new THREE.Scene();

  const camera = new THREE.PerspectiveCamera(
    55,
    window.innerWidth / window.innerHeight,
    0.1,
    3000,
  );
  camera.position.set(0, 5, 16);

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 6;
  controls.maxDistance = 60;
  controls.autoRotate = !prefersReducedMotion;
  controls.autoRotateSpeed = 0.4;

  scene.add(createStarfield());
  scene.add(createEventHorizon());
  scene.add(createGlow());

  const mainDisk = createDisk(HORIZON_RADIUS * 1.6, HORIZON_RADIUS * 4.2, 1);
  mainDisk.rotation.x = Math.PI / 2.3;
  scene.add(mainDisk);

  // A thin, always-in-front ring standing in for the gravitationally
  // lensed photon ring that (in reality) wraps light from the far side
  // of the disk over the poles of the black hole.
  const lensedRing = createDisk(HORIZON_RADIUS * 1.15, HORIZON_RADIUS * 1.55, 0.6);
  lensedRing.material.depthTest = false;
  lensedRing.renderOrder = 10;
  scene.add(lensedRing);

  const composer = new EffectComposer(renderer);
  composer.addPass(new RenderPass(scene, camera));

  const lensingPass = new ShaderPass(LensingShader);
  lensingPass.uniforms.uCenter.value = new THREE.Vector2(0.5, 0.5);
  lensingPass.uniforms.uAspect.value = window.innerWidth / window.innerHeight;
  composer.addPass(lensingPass);

  const bloomPass = new UnrealBloomPass(
    new THREE.Vector2(window.innerWidth, window.innerHeight),
    0.55,
    0.4,
    0.3,
  );
  composer.addPass(bloomPass);

  const originScreen = new THREE.Vector3();
  const clock = new THREE.Clock();

  function animate() {
    requestAnimationFrame(animate);
    const elapsed = clock.getElapsedTime() * motionScale;

    mainDisk.material.uniforms.uTime.value = elapsed;
    lensedRing.material.uniforms.uTime.value = elapsed * 1.3;

    originScreen.set(0, 0, 0).project(camera);
    lensingPass.uniforms.uCenter.value.set(
      (originScreen.x + 1) / 2,
      (originScreen.y + 1) / 2,
    );

    controls.update();
    composer.render();
  }
  animate();

  window.addEventListener("resize", () => {
    const width = window.innerWidth;
    const height = window.innerHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
    composer.setSize(width, height);
    lensingPass.uniforms.uAspect.value = width / height;
  });
}

function createStarfield() {
  const count = 6000;
  const positions = new Float32Array(count * 3);
  for (let i = 0; i < count; i++) {
    const radius = 400 + Math.random() * 900;
    const theta = Math.random() * Math.PI * 2;
    const phi = Math.acos(2 * Math.random() - 1);
    positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
    positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
    positions[i * 3 + 2] = radius * Math.cos(phi);
  }
  const geometry = new THREE.BufferGeometry();
  geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
  const material = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 1.4,
    sizeAttenuation: true,
    transparent: true,
    opacity: 0.85,
  });
  return new THREE.Points(geometry, material);
}

function createEventHorizon() {
  const geometry = new THREE.SphereGeometry(HORIZON_RADIUS, 64, 64);
  const material = new THREE.MeshBasicMaterial({ color: 0x000000 });
  return new THREE.Mesh(geometry, material);
}

function createGlow() {
  const geometry = new THREE.SphereGeometry(HORIZON_RADIUS * 1.08, 64, 64);
  const material = new THREE.ShaderMaterial({
    uniforms: { glowColor: { value: new THREE.Color(0xffb066) } },
    vertexShader: glowVertexShader,
    fragmentShader: glowFragmentShader,
    side: THREE.BackSide,
    blending: THREE.AdditiveBlending,
    transparent: true,
    depthWrite: false,
  });
  return new THREE.Mesh(geometry, material);
}

function createDisk(innerRadius, outerRadius, brightness) {
  const geometry = new THREE.RingGeometry(innerRadius, outerRadius, 128, 1);
  const material = new THREE.ShaderMaterial({
    uniforms: {
      uTime: { value: 0 },
      uBrightness: { value: brightness },
      innerRadius: { value: innerRadius },
      outerRadius: { value: outerRadius },
    },
    vertexShader: diskVertexShader,
    fragmentShader: diskFragmentShader,
    side: THREE.DoubleSide,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false,
  });
  return new THREE.Mesh(geometry, material);
}
