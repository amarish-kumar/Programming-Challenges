class Person {
    public int age;
	public Person(int initialAge) {
        if (isPositive (initialAge)) {
            this.age = initialAge;
        } else {
            this.age = 0;
        }
    }
    
    public void amIOld() {
        // Do some computations in here and print out the correct statement to the console 
        if (this.age < 13) {
            Console.WriteLine ("You are young.");
        } else if (this.age < 18) {
            Console.WriteLine ("You are a teenager.");
        } else {
            Console.WriteLine ("You are old.");
        }
    }

    public void yearPasses() {
        // Increment the age of the person in here
        this.age += 1;
    }
    
    private bool isPositive (int age) {
        if (age > 0) {
            return (true);
        }
        
        Console.WriteLine ("Age is not valid, setting age to 0.");
        return (false);
    }
