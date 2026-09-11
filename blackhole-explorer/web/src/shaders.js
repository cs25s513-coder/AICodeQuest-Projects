export const glowVertexShader = `
  varying vec3 vNormal;
  varying vec3 vViewPosition;
  void main() {
    vNormal = normalize(normalMatrix * normal);
    vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
    vViewPosition = -mvPosition.xyz;
    gl_Position = projectionMatrix * mvPosition;
  }
`;

export const glowFragmentShader = `
  uniform vec3 glowColor;
  varying vec3 vNormal;
  varying vec3 vViewPosition;
  void main() {
    float intensity = pow(0.6 - dot(normalize(vNormal), normalize(vViewPosition)), 4.0);
    gl_FragColor = vec4(glowColor, clamp(intensity, 0.0, 1.0) * 0.6);
  }
`;

export const diskVertexShader = `
  uniform float innerRadius;
  uniform float outerRadius;
  varying float vRadius;
  varying float vAngle;
  void main() {
    float r = length(position.xy);
    vRadius = clamp((r - innerRadius) / (outerRadius - innerRadius), 0.0, 1.0);
    vAngle = atan(position.y, position.x);
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;

export const diskFragmentShader = `
  uniform float uTime;
  uniform float uBrightness;
  varying float vRadius;
  varying float vAngle;

  vec3 diskColor(float r) {
    vec3 hot = vec3(1.0, 0.98, 0.92);
    vec3 mid = vec3(1.0, 0.62, 0.22);
    vec3 cool = vec3(0.55, 0.14, 0.05);
    vec3 inner = mix(hot, mid, smoothstep(0.0, 0.45, r));
    vec3 outer = mix(mid, cool, smoothstep(0.45, 1.0, r));
    return mix(inner, outer, step(0.45, r));
  }

  void main() {
    float swirl = sin(vAngle * 8.0 - uTime * 1.4 + vRadius * 20.0) * 0.12
                + sin(vAngle * 3.0 + uTime * 0.6) * 0.08;
    float r = clamp(vRadius + swirl * (1.0 - vRadius), 0.0, 1.0);

    vec3 color = diskColor(r);
    float innerFade = smoothstep(0.0, 0.06, vRadius);
    float outerFade = 1.0 - smoothstep(0.82, 1.0, vRadius);
    float alpha = innerFade * outerFade;
    float brightness = mix(1.5, 0.25, vRadius) * uBrightness;

    gl_FragColor = vec4(color * brightness, alpha);
  }
`;

export const LensingShader = {
  uniforms: {
    tDiffuse: { value: null },
    uCenter: { value: null },
    uAspect: { value: 1.0 },
    uStrength: { value: 0.045 },
  },
  vertexShader: `
    varying vec2 vUv;
    void main() {
      vUv = uv;
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `,
  fragmentShader: `
    uniform sampler2D tDiffuse;
    uniform vec2 uCenter;
    uniform float uAspect;
    uniform float uStrength;
    varying vec2 vUv;

    void main() {
      vec2 toCenter = vUv - uCenter;
      toCenter.x *= uAspect;
      float dist = length(toCenter) + 0.0005;
      float bend = uStrength / (dist * dist * 18.0 + 1.0);
      vec2 dir = toCenter / dist;
      dir.x /= uAspect;
      vec2 warped = clamp(vUv - dir * bend, 0.001, 0.999);
      gl_FragColor = texture2D(tDiffuse, warped);
    }
  `,
};
