var flipAndInvertImage = function(image) 
{
    let change = [1, 0];
    image.map((a) => a.reverse()).forEach((t, i) => image[i] = t = t.map((b) => change[b]));
    return image;
};