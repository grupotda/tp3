#pragma once

#include <vector>
#include "Knapsack.h"

class KnapsackApprox
{
private:
    int m_profit; // ganancia aproximada
    Knapsack* m_knapsack; // prog. dinamica
public:
    KnapsackApprox(const std::vector<item_t>& items, int capacity, double e);
    ~KnapsackApprox();
    // Devuelve la ganancia.
    int profit() {return m_profit;};
    // Devuelve el peso asociado a la ganancia.
    int weight() {return m_knapsack->weight();};
    // Devuelve un arreglo del tamaño de items que indica si en esa posicion
    // el elemento de items esta en la solucion.
    const std::vector<bool>& solution() {return m_knapsack->solution();};
};

