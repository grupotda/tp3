#include <iostream>
#include <algorithm>
#include <cstddef>
#include "KnapsackApprox.h"

KnapsackApprox::KnapsackApprox(const std::vector<item_t>& items, int capacity, double e)
{
    // Tomamos el mayor valor de los elementos:
    int max_value = 0;
    for (const item_t& item : items) {
        if (item.value > max_value) {
            max_value = item.value;
        }
    }

    // Metodo kleinberg (con ceiling):
    double b = (e / (2*items.size())) * max_value;

    if (b > 1.0) { // Tiene sentido aproximar
        // Generamos los nuevos valores:
        std::vector<item_t> temp_items(items);
        for (item_t& item : temp_items) {
            item.value = (int) ceil(item.value / b);
        }

        // Calculamos:
        m_knapsack = new Knapsack(temp_items, capacity);
        m_profit = 0;
        auto sol = m_knapsack->solution();
        for (size_t i = 0; i < sol.size(); ++i) {
            if (sol[i]) m_profit += items[i].value;
        }

    } else { // Es equivalente a calcular el optimo
        m_knapsack = new Knapsack(items, capacity);
        m_profit = m_knapsack->profit();
    } 
}

KnapsackApprox::~KnapsackApprox() {
    delete m_knapsack;
}
