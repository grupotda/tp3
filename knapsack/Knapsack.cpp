#include <iostream>
#include <cstddef>
#include "Knapsack.h"

Knapsack::Knapsack(const std::vector<item_t>& items, int capacity):
    m_kept(std::vector<bool>(items.size(), false))
{   
    // Un arreglo de sumatorias de los valores de los items:
    std::vector<int> sum_values(items.size() + 1);

    sum_values[0] = 0;
    for (size_t i = 1; i < sum_values.size(); ++i) {
        sum_values[i] = sum_values[i-1] + items[i-1].value;
    }

    // Solo un arreglo de peso por ganancia minima asegurada, iteramos al reves para saber valores anteriores
    std::vector<int> weights(sum_values.back() + 1, capacity + 1);
    weights[0] = 0;

    // vector<bool> es un "dynamic bitset" eficiente en espacio, para saber si esta o no el item
    std::vector<std::vector<bool>> keep(items.size(), std::vector<bool>(weights.size(), false));

    for (size_t i = 0; i < items.size(); ++i) {
        int v = sum_values[i+1];

        for (; v > sum_values[i] && v > items[i].value; --v) { // agregar siempre
            weights[v] = items[i].weight + weights[v - items[i].value];
            keep[i][v] = true;
        }

        for (; v > sum_values[i]; --v) { // agregar siempre
            weights[v] = items[i].weight;
            keep[i][v] = true;
        }

        for (; v > items[i].value; --v) { // soy agregable, comparar restando mi valor
            if (items[i].weight + weights[v - items[i].value] < weights[v]) {
                weights[v] = items[i].weight + weights[v - items[i].value];
                keep[i][v] = true;
            }
        }

        for (; v > 0; --v) { // entro solo o es mejor lo anterior
            if (items[i].weight < weights[v]) {
                weights[v] = items[i].weight;
                keep[i][v] = true;
            }
        }
    }

    //Calculamos la primer ganancia minima segun capacity:
    int v = weights.size() - 1;
    while (weights[v] > capacity) --v;

    m_weight = weights[v];
    m_profit = v; // Aseguramos que es la mejor porque al proximo cambia el peso

    //Identificamos los elementos en la mochila
    for (size_t i = items.size(); i --> 0;) { // i>0;) { i--; ... }
        if (keep[i][v]) {
            v -= items[i].value;
            m_kept[i] = true;
        }
    }

}

Knapsack::~Knapsack() {}
