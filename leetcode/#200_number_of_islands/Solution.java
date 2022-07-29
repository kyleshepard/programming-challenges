import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int numIslands(char[][] grid) {
        int islands = 0;
        int width = grid.length;
        int height = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        
        //look over every item
        for(int i = 0; i < width; i++){
            for(int j = 0; j < height; j++){
                
                //if it is unvisited and a piece of land, add 1 to island count and identify the rest
                if(grid[i][j] == '1'){
                    // System.out.println("found land");
                    islands++;
                    queue.add(new int[]{i, j});
                    grid[i][j] = '0';
                }
                
                //use bfs to find other pieces of connected land
                while(!queue.isEmpty()){
                    
                    //remove from queue and mark as visited
                    int[] p = queue.remove();
                    
                    //look in all 4 cardinal directions. if neighbor is in bounds, a piece of land, and unvisited, add it to the queue
                    
                    //left (x-1)
                    if(0 < p[0] && grid[p[0]-1][p[1]] == '1'){
                        int[] point = new int[]{p[0]-1, p[1]};
                        queue.add(point);
                        grid[point[0]][point[1]] = '0';
                    }
                    
                    //up (y-1)
                    if(0 < p[1] && grid[p[0]][p[1]-1] == '1'){
                        int[] point = new int[]{p[0], p[1]-1};
                        queue.add(point);
                        grid[point[0]][point[1]] = '0';
                    }
                    
                    //right (x+1)
                    if(width-1 > p[0] && grid[p[0]+1][p[1]] == '1'){
                        int[] point = new int[]{p[0]+1, p[1]};
                        queue.add(point);
                        grid[point[0]][point[1]] = '0';
                    }
                    
                    //down (y+1)
                    if(height-1 > p[1] && grid[p[0]][p[1]+1] == '1'){
                        int[] point = new int[]{p[0], p[1]+1};
                        queue.add(point);
                        grid[point[0]][point[1]] = '0';
                    }
                }
            }   
        }
        
        return islands;
    }
}