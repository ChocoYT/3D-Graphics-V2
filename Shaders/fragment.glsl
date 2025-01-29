#version 330 core

in vec3 normal;
in vec2 UV;

uniform sampler2D tex;
uniform float time;

out vec4 frag_color;

void main()
{
  vec4 objectColor = vec4(0.5, 0.5, 0.5,1);
  vec4 lightColor = vec4(1, 1, 1,1);

  vec3 lightDir = vec3(sin(time) * 100.0, 0, cos(time) * 100.0);
  float NdotL = dot(normalize(normal), normalize(lightDir));

  float diffuseIntensity = 1.0;
  float ambientIntensity = 1.0;

  vec4 ambient = objectColor * vec4(vec3(ambientIntensity), 1);
  vec4 diffuse = objectColor * lightColor * NdotL * diffuseIntensity;

  frag_color = texture(tex, UV) * (ambient + diffuse);
}