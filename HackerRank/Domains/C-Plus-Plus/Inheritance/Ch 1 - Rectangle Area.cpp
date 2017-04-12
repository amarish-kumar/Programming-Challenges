class Rectangle {
    public:
        int width;
        int height;
        
        void Display () {
            cout << width << " " << height << "\n";
        }
};

class RectangleArea : public Rectangle {
    public:
        void Input () {
            scanf("%d %d", &width, &height);
        }
        void Display () {
            cout << width * height;
        }
};
