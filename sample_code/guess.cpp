//GUESS

//header files
#include<iostream>
#include<cmath>
#include<cstdlib>
#include<ctime>
using namespace std;


//main function
int main()
{
	int x=1;
	
	while (x==1) {
	//declare variables
	int guess;
	int actual; 
	int low;
	int high;
	int score = 0;
	int counter = 0;

	
	
	//user prompt
	cout << "High?" << endl;
	cin >> high;
	cout << "Low?" << endl;
	cin >> low;
	
	//set random value
	srand(time(NULL));
	actual = rand() % high + low; 
	
	//guess loop
	do
	{
		//prompt
		cout << "Guess a number: " << endl;
		cin >> guess;
		
		if (guess == actual)
		{
			score += 10;
			cout << "Correct!" << endl; 
			cout << "Number of wrong answers: " << counter << endl;
			cout << "Final score: " << score << endl;
			cout << "Enter 1 to play again. Enter 0 to quit: " << endl;
			cin >> x;
		}
	
		else if (guess > actual)
		{
		cout << "Wrong. Too high!" << endl;
		counter++;
		score -= 1; 
		}
		
		else
		{
			cout << "Wrong. Too low!" << endl;
			counter++;
			score -= 1;
		}
		
	} while (guess != actual);
	
	}

	return 0;
}
