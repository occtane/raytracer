#include "color.h"
#include "vec3.h"

#include <iostream>

int main()
{
    // Image
    int image_width = 256;
    int image_height = 256;

    // Render
    std::cout << "P3\n"
              << image_width << ' ' << image_height << "\n255\n";

    for (int j = 0; j < image_height; ++j)
    {
        std::clog << "\rScanlines remaining: " << (image_height - j) << ' ' << std::flush;
        for (int i = 0; i < image_width; ++i)
        {
            // Cast each pixel (i and j) into double and divide it by 255.
            // This way we get a range from 0.0 and 1.0 for the colors.
            auto pixel_color = color(double(i) / (image_width - 1), double(j) / (image_height - 1), 0);
            write_color(std::cout, pixel_color);
        }
    }

    std::clog << "\rDone.                 \n";

    return 0;
}