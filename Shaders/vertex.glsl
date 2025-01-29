#version 330 core

in vec3 position;
in vec3 vertex_normal;

uniform mat4 projection_mat;
uniform mat4 view_mat;
uniform mat4 model_mat;

out vec3 normal;

void main()
{
    gl_Position = projection_mat * view_mat * model_mat * vec4(position, 1);
    normal = mat3(model_mat) * vertex_normal;
}