// Calculate the arithmetic mean of non-empty integer scores.
#include <iostream>
#include <numeric>
#include <vector>

double averageScore(const std::vector<int>& scores) {
    int total = std::accumulate(scores.begin(), scores.end(), 0);
    return total / scores.size();
}

int main() {
    const std::vector<int> scores{4, 4, 5};
    const double mean = averageScore(scores);
    std::cout << "Average: " << mean << '\n';
    std::cout << "Expected: 4.33333..." << '\n';
    return 0;
}
