public class Co_ord {
    int x;
    int y;
    int max;

    public Co_ord(int x, int y, int max) {
        if (max < 1 || x < 1 || x > max || y < 1 || y > max)
            throw new NumberFormatException();
        this.x = x;
        this.y = y;
        this.max = max;
    }

    public Co_ord(int x, int y, int max, int min) {
        if (max < min || x < min || x > max || y < min || y > max)
            throw new NumberFormatException();
        this.x = x;
        this.y = y;
        this.max = max;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null || getClass() != obj.getClass())
            return false;
        Co_ord c = (Co_ord) obj;
        return (c.x == this.x && c.y == this.y);
    }

    public int x_to_list() {
        return x - 1;
    }

    public int y_to_list() {
        return max - y;
    }

}
