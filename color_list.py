import colorgram

# making a colors_list of tuples of RGB colors without the first colors that are the background, white variations
colors = colorgram.extract('hirst_painting.jpg', 20)
rgb_tuples = [(colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b) for i in range(len(colors))]
colors_list = rgb_tuples[5:]