#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;

class ATM
{
private:
    string accountHolder;
    string address;
    string branch;
    int accountNumber;
    int pin;
    double initialBalance;
    double currentBalance;

public:
    ATM();
    void showWelcomeScreen();
    void showHelpScreen();
    bool verifyPin();
    void mainMenu();
    void depositCash();
    void withdrawCash();
    void balanceInquiry();
    void exitMessage();
    void accountDetails(string title);
};

ATM::ATM()
{
    accountHolder = "Anshu Patel";
    address = "Ahmedabad";
    branch = "Vastral";
    accountNumber = 5678;
    pin = 12345;
    initialBalance = 60000;
    currentBalance = 20000;
}

void ATM::showWelcomeScreen()
{
    time_t now = time(0);
    char *dt = ctime(&now);

    cout << "\n=========================================\n";
    cout << "            WELCOME TO ATM               \n";
    cout << "=========================================\n";
    cout << "Current Date and Time : " << dt;
    cout << "-----------------------------------------\n";
    cout << "Press 1 and then Enter to Access Account\n";
    cout << "Press 2 and then Enter to Get Help\n";
    cout << "Press 0 and then Enter to Exit\n";
    cout << "-----------------------------------------\n";
}

void ATM::showHelpScreen()
{
    cout << "\n=========================================\n";
    cout << "           ATM ACCOUNT STATUS            \n";
    cout << "=========================================\n";
    cout << "You must have the correct PIN number\n";
    cout << "to access this account.\n";
    cout << "See your bank representative for help\n";
    cout << "during bank opening hours.\n";
    cout << "Thanks for your choice today!!\n";
    cout << "=========================================\n";
}

bool ATM::verifyPin()
{
    int enteredPin;
    cout << "\n=========================================\n";
    cout << "          ATM ACCOUNT ACCESS             \n";
    cout << "=========================================\n";
    cout << "Enter Your Account PIN Number\n";
    cout << "[Only one attempt is allowed]: ";
    cin >> enteredPin;

    if (enteredPin == pin)
    {
        return true;
    }
    else
    {
        cout << "\n=========================================\n";
        cout << "               THANK YOU                 \n";
        cout << "=========================================\n";
        cout << "You had made your attempt which failed.\n";
        cout << "No more attempts allowed!! Sorry!!\n";
        cout << "=========================================\n";
        return false;
    }
}

void ATM::accountDetails(string title)
{
    cout << "\n=========================================\n";
    cout << "        " << title << "\n";
    cout << "=========================================\n";
    cout << "Account Holder Name : " << accountHolder << endl;
    cout << "Account Holder Address : " << address << endl;
    cout << "Branch Location : " << branch << endl;
    cout << "Account Number : " << accountNumber << endl;
    cout << "Initial Starting Balance : Rs. " << initialBalance << endl;
    cout << "Present Available Balance : Rs. " << currentBalance << endl;
    cout << "-----------------------------------------\n";
}

void ATM::depositCash()
{
    double amount;
    accountDetails("ATM ACCOUNT DEPOSIT SYSTEM");
    cout << "Enter Amount to Deposit : Rs. ";
    cin >> amount;

    if (amount > 0)
    {
        currentBalance += amount;
        cout << "Your new available balance is Rs. " << currentBalance << endl;
        cout << "Thank You!\n";
    }
    else
    {
        cout << "Invalid deposit amount.\n";
    }
}

void ATM::withdrawCash()
{
    double amount;
    accountDetails("ATM ACCOUNT WITHDRAWAL");
    cout << "Enter Amount to Withdraw : Rs. ";
    cin >> amount;

    if (amount <= 0)
    {
        cout << "Invalid withdrawal amount.\n";
    }
    else if (amount > currentBalance)
    {
        cout << "\nInsufficient Available Balance in your account.\n";
        cout << "Sorry !!\n";
    }
    else
    {
        currentBalance -= amount;
        cout << "Please collect your cash.\n";
        cout << "Your new available balance is Rs. " << currentBalance << endl;
        cout << "Thank You!\n";
    }
}

void ATM::balanceInquiry()
{
    cout << "\n=========================================\n";
    cout << "            BALANCE INQUIRY              \n";
    cout << "=========================================\n";
    cout << "Account Holder Name : " << accountHolder << endl;
    cout << "Account Number : " << accountNumber << endl;
    cout << "Initial Starting Balance : Rs. " << initialBalance << endl;
    cout << "Present Available Balance : Rs. " << currentBalance << endl;
    cout << "=========================================\n";
}

void ATM::exitMessage()
{
    cout << "\n=========================================\n";
    cout << "      Thank you for using this ATM       \n";
    cout << "=========================================\n";
}

void ATM::mainMenu()
{
    int choice;

    do
    {
        cout << "\n=========================================\n";
        cout << "            ATM MAIN MENU                \n";
        cout << "=========================================\n";
        cout << "Enter [1] To Deposit Cash\n";
        cout << "Enter [2] To Withdraw Cash\n";
        cout << "Enter [3] To Balance Inquiry\n";
        cout << "Enter [0] To Exit ATM\n";
        cout << "-----------------------------------------\n";
        cout << "Please Enter a Selection: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            depositCash();
            break;
        case 2:
            withdrawCash();
            break;
        case 3:
            balanceInquiry();
            break;
        case 0:
            exitMessage();
            break;
        default:
            cout << "Invalid choice. Please try again.\n";
        }

    } while (choice != 0);
}

int main()
{
    ATM atm;
    int firstChoice;

    atm.showWelcomeScreen();
    cout << "Enter your choice: ";
    cin >> firstChoice;

    switch (firstChoice)
    {
    case 1:
        if (atm.verifyPin())
        {
            atm.mainMenu();
        }
        break;

    case 2:
        atm.showHelpScreen();
        break;

    case 0:
        atm.exitMessage();
        break;

    default:
        cout << "Invalid choice.\n";
    }

    return 0;
}
