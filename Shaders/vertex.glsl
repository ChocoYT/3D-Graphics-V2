#version 330 core

in vec3 position;
in vec3 vertex_normal;
in vec2 vertex_uv;

uniform mat4 projection_mat;
uniform mat4 view_mat;
uniform mat4 model_mat;

out vec3 normal;
out vec2 UV;

void main()
{
    gl_Position = projection_mat * view_mat * model_mat * vec4(position, 1);

    UV = vertex_uv;
    normal = mat3(model_mat) * vertex_normal;
}