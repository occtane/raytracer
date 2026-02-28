#pragma once

#include "vec3.h"

#include <iostream>

using color = vec3;

void write_color(std::ostream &out, const color &pixel_color)
{
    // Saving each xyz component to its corresponding rgb
    auto r = pixel_color.x();
    auto g = pixel_color.y();
    auto b = pixel_color.z();

    // Translate the [0,1] component values to the byte range [0,255] to make use for RGB colors
    int rbyte = int(255.999 * r);
    int gbyte = int(255.999 * g);
    int bbyte = int(255.999 * b);

    // Write out the pixel color components
    out << rbyte << ' ' << gbyte << ' ' << bbyte << '\n';
}