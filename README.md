# fractals
Multiple python pygame programs for drawing different fractals

# Fractal tree
Program for drawing [fractal trees](https://en.wikipedia.org/wiki/Fractal_canopy) in Pygame

### Configuration
At the beginning of the `main()` function, you’ll find several constants such as:
- `ANGLE` — branch rotation angle (in radians)
- `RATIO` — branch length ratio
- `DEPTH` — recursion depth
- `START_LENGTH` — starting branch length

Modify these to create trees of different shapes and complexity.

# Mandelbrot set
Drawing [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) in pygame

### Configuration
On the top of `main()` function there are 2 constants you can change:
- `NUMBER_OF_ITERATIONS` - change number of iterations per pixel, higher the number, higher the resolution, but slower generation (try using from 100 to 1000)
- `COLOR` - color of the Mandelbrot set

![Mandelbrot set](https://github.com/RedDoughnut/fractals/blob/main/MandelbrotSet.png)

# Koch snowflake
Drawing [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake) in pygame

You can change `DELAY` (in seconds) which is the time delay between steps of Koch snowflake
