using System;
using System.Collections.Generic;
using System.IO;
class Solution {

    static void nextMove(int n,int r, int c, String [] grid)
    {
        var levelPeach = 0;
        var peachPosition = 0;
        var marioPosition = 0;
        
        var levelMario = 0;
        for (int i = 0; i < grid.Length; i++)
        {
            if (grid[i].Contains("p"))
            {
                levelPeach = i;
                peachPosition = grid[i].IndexOf('p');
            }
            if (grid[i].Contains("m"))
            {
                levelMario = i;
                marioPosition = grid[i].IndexOf('m');
            }
        }
        
        if (levelMario < levelPeach)
        {
            Console.WriteLine("DOWN");
        }
        else if (levelMario > levelPeach)
        {
            Console.WriteLine("UP");
        }
        else
        {
            if (marioPosition < peachPosition)
            {
                Console.WriteLine("RIGHT");
            }
            else if (marioPosition > peachPosition)
            {
                Console.WriteLine("LEFT");
            }
        }
    }

    static void Main(String[] args) {
        int n;

        n = int.Parse(Console.ReadLine());
        String pos;
        pos = Console.ReadLine();
        String[] position = pos.Split(' ');
        int [] int_pos = new int[2];
        int_pos[0] = Convert.ToInt32(position[0]);
        int_pos[1] = Convert.ToInt32(position[1]);
        String[] grid  = new String[n];
        for(int i=0; i < n; i++) {
            grid[i] = Console.ReadLine(); 
        }

        nextMove(n, int_pos[0], int_pos[1], grid);
    }
}
