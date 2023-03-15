/**
 * @param {number[][]} grid
 * @return {boolean}
 */
var checkXMatrix = function(grid) 
{
    for(let i = 0; i < grid.length; i++)
    {
        if(grid[i][i] === 0 || grid[grid.length - i - 1][i] === 0)
        {
            return false;
        }
        grid[i][i] = 0;
        grid[grid.length - i - 1][i] = 0;
    }

    return grid.flat(1).reduce((p, cur) => p + Math.abs(cur), 0) === 0;
};
