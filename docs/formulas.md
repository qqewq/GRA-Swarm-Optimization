# Формулы GRA-Обнуленки

## 1. Hierarchical Stability (S_h)

$$
S_h = \prod_{i=1}^{n} \frac{H_i}{H_{i-1}} \cdot e^{-\lambda \cdot \Delta H_i}
$$

- $H_i$ – уровень иерархии
- $\Delta H_i = H_i - H_{i-1}$
- $\lambda$ – коэффициент стабильности
- Условие: $S_h \ge S_{threshold}$ – система стабильна.

## 2. Subjectivity ($\mathcal{S}$)

$$
\mathcal{S} = \int_{\Omega} \rho(x) \cdot \log\left(\frac{\rho(x)}{\mu(x)}\right) dx
$$

- $\rho(x)$ – распределение агента
- $\mu(x)$ – распределение среды
- Условие: $\mathcal{S} > 0$ – агент обладает субъектностью.

## 3. Nullification ($\mathcal{N}$)

$$
\mathcal{N}(E) = \exp\left(-\beta \cdot \|E - E_{optimal}\|^2\right)
$$

- $E$ – ошибка
- $E_{optimal}$ – оптимальная ошибка (0)
- $\beta$ – коэффициент обнуления
- Условие: $\mathcal{N}(E) \to 1$ – ошибка обнулена.

## 4. Гёделевское пространство решений ($\mathcal{G}$)

$$
\mathcal{G} = \{x \in X \mid \phi(x) \text{ доказуемо в GRA}\}
$$

Оптимизация:

$$
\mathcal{G}_{optimal} = \arg\max_{x \in \mathcal{G}} \left[ S_h(x) \cdot \mathcal{S}(x) \cdot \mathcal{N}(E(x)) \right]
$$

## 5. Рекурсивная оптимизация ($\mathcal{O}$)

$$
\mathcal{O}^{(k+1)} = \arg\max_{\mathcal{O}^{(k)}} \left[ \mathcal{G}_{optimal}(\mathcal{O}^{(k)}) \right]
$$

Полная оптимизация:

$$
\mathcal{O}^{(\infty)} = \lim_{k \to \infty} \mathcal{O}^{(k)}
$$
