package num_islands

import (
	"fmt"
	"testing"
)

func TestNumIslands(t *testing.T) {
	var tests = []struct {
		grid [][]byte
		want int
	}{
		{
			grid: [][]byte{
				{'1','1','1','1','0'},
				{'1','1','0','1','0'},
				{'1','1','0','0','0'},
				{'0','0','0','0','0'},
			},
			want: 1,
		},
		{
			grid: [][]byte{
				{'1','1','0','0','0'},
				{'1','1','0','0','0'},
				{'0','0','1','0','0'},
				{'0','0','0','1','1'},
			},
			want: 3,
		},
	}

	for _, tt := range tests {
		testname := fmt.Sprintf("%d islands", tt.want)
		t.Run(testname, func(t *testing.T) {
			res := numIslands(tt.grid)
			if res != tt.want {
				t.Errorf("numIslands got %d, want = %d", res, tt.want)
			}
		})
	}
}
