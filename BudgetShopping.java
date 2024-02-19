public class BudgetShopping {

    public static long countPurchases(int[] costs, long budget) {
        long purchases = 0;
        boolean canPurchase = true;

        while (canPurchase) {
            canPurchase = false; // Assume no purchase can be made initially
            for (int cost : costs) {
                if (cost <= budget) {
                    budget -= cost; // Deduct the cost from the budget
                    purchases++; // Increment the purchase count
                    canPurchase = true; // A purchase was made, so we might continue
                }
            }
        }

        return purchases;
    }

    public static void main(String[] args) {
        int[] costs = { 2, 4, 100, 2, 6 };
        long budget = 21;
        System.out.println("Total purchases: " + countPurchases(costs, budget));
    }
}
