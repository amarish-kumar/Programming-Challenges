class Student {
    private:
        int scores[5];
    public:
        void Input () {
            scanf("%d %d %d %d %d", &scores[0], &scores[1], &scores[2], &scores[3], &scores[4]);
        }
        int CalculateTotalScore () {
            int sum = 0;
            for (int i = 0; i < 5; i++) {
                sum += scores[i];
            }
            return (sum);
        }
};
