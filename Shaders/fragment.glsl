#version 330 core

in vec3 normal;

uniform float time;

out vec4 frag_color;

void main()
{
  vec4 objectColor = vec4(0.5, 0.5, 0.5, 1);
  vec4 lightColor = vec4(1, 1, 1,1);

  vec3 lightDir = vec3(sin(time) * 10.0, 0, cos(time) * 10.0);
  float NdotL = dot(normalize(normal), normalize(lightDir));

  float intensity = 3;
  vec4 diffuse = lightColor * (NdotL * intensity);

  frag_color = objectColor * diffuse;
}