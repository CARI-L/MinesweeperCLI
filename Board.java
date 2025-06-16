import java.util.ArrayList;

public class Board {
    int length;
    int width;
    ArrayList<ArrayList<Plot>> field;

    public Board(int size) {
        if(size <= 0) throw new NumberFormatException();
        length = size;
        width = size;

    }

    public Board(int length, int width) {
        if(length <= 0 || width <= 0) throw new NumberFormatException();
        this.length = length;
        this.width = width;

    }

    public void randomBoard(int count) {

        field = new ArrayList<>();
        for(int i = 0; i < length; i++) {
            field.add(new ArrayList<Plot>());
            for(int j = 0; j < width; j++) field.get(i).add(new Plot());
        }

        if(count <= 0) throw new NumberFormatException();
        while(count > 0) {
            Plot target = field.get(randInt(length-1)).get(randInt(width-1));
            switch(target.value){
                case 9:
                default: 
                    target.value = 9;
                    count--;
            }
        }

        for(int i = 0; i < length; i++) {
            ArrayList<Integer> adj_i = new ArrayList<>();
            adj_i.add(0);
            if(i == 0) adj_i.add(1);
            else if (i == length-1) adj_i.add(-1);
            else {
                adj_i.add(1);
                adj_i.add(-1);
            }

            for(int j = 0; j < width; j++) {
                if(field.get(i).get(j).value == 9) continue;

                ArrayList<Integer> adj_j = new ArrayList<>();
                adj_j.add(0);
                if(j == 0) adj_j.add(1);
                else if (j == width-1) adj_j.add(-1);
                else {
                    adj_j.add(1);
                    adj_j.add(-1);
                }  

                for(int off_i : adj_i) {
                    for(int off_j: adj_j) {
                        if(off_i == 0 && off_j == 0) continue;
                        if(field.get(i+off_i).get(j+off_j).value == 9) field.get(i).get(j).value++;
                    }
                }
            }
        }
    }

    // dig function HERE

    @Override
    public String toString(){
        String result = "";
        for(int i = 0; i < length; i++) {
            for(int j = 0; j < width; j++) {
                if(j == 0) result += String.format("%d   |", (length - i));
                result += field.get(i).get(j) + "|";
            }
            result += "\n";
        }
        result += "\n    ";
        for(int i = 1; i <= width; i++) result += " " + i;

        return result;
    }

    int randInt(int max){
        return (int) Math.round(Math.random() * max);
    }
}
