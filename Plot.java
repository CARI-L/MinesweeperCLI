public class Plot {
    State state;
    int value;

    public Plot(){
        state = State.COVERED;
        value = 0;
    }

    @Override
    public String toString(){
        switch(state){
            case COVERED: return "■";
            case FLAGGED: return "⚑";
            case UNCOVERED: 
                switch(value){
                    case 0: return " ";
                    case 9: return "☠";
                    default: return Integer.toString(value);
                }
            default: return Integer.toString(value);
        }
}
}
