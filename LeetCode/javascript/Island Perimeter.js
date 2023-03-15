var islandPerimeter = function(grid) {
    
    let toRt = [];

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) 
        {
            let el = grid[i][j];
            if(el === 0){continue;}

            let adj = getAdjacent(i, j);

            toRt.push(adj);
        }
    }
    
    function getAdjacent(i, j){
        let up = grid[i - 1];
        let down = grid[i + 1];

        return [grid[i][j - 1], grid[i][j + 1], up? up[j] : undefined, down? down[j] : undefined];
    }
    
    return toRt.flat(1).map((a) => a == undefined || a == 0? 1 : 0).reduce((a , b) => {return a + b}, 0);
};