#include <stdio.h>

int main() {
    int choice, qty;
    char more;
    float total = 0;

    do {
        // Display menu
        printf("\n===== FOOD MENU =====\n");
        printf("1. Pizza      - Rs. 120\n");
        printf("2. Burger     - Rs. 80\n");
        printf("3. Sandwich   - Rs. 70\n");
        printf("4. Cold Drink - Rs. 40\n");
        printf("5. Ice Cream  - Rs. 60\n");
        printf("======================\n");

        // Take item choice
        printf("Enter item number: ");
        scanf("%d", &choice);

        // Take quantity
        printf("Enter quantity: ");
        scanf("%d", &qty);

        // Business logic for billing
        switch (choice) {
            case 1:
                total += 120 * qty;
                break;
            case 2:
                total += 80 * qty;
                break;
            case 3:
                total += 70 * qty;
                break;
            case 4:
                total += 40 * qty;
                break;
            case 5:
                total += 60 * qty;
                break;
            default:
                printf("Invalid choice!\n");
        }

        // Ask if user wants more items
        printf("\nDo you want to order more? (y/n): ");
        scanf(" %c", &more);

    } while (more == 'y' || more == 'Y');

    // Final bill display
    printf("\n===== FINAL BILL =====\n");
    printf("Total Amount = Rs. %.2f\n", total);
    printf("======================\n");

    return 0;
}
