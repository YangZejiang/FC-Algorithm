# Fitness - Complexity Algorithm

This iterative method is composed of two steps at each iteration: we first compute the intermediate variables $\tilde{F}_{c}^{(n)}$ and $\tilde{Q}_{p}^{(n)}$ and then normalize them. The initial conditions are $\tilde{Q}_{p}^{(0)}=1$  $\forall p$ and $\tilde{F}_{c}^{(0)}=1$  $\forall c$.

Step1
$$
\begin{aligned}
&\tilde{F}_{c}^{(n)}=\sum{ }_{p} M_{c p} Q_{p}^{(n-1)} \\
&\tilde{Q}_{p}^{(n)}=\frac{1}{\sum{ }_{c} M_{c p} \frac{1}{F_{c}^{(n-1)}}}
\end{aligned}
$$
Step2
$$
\begin{aligned} F_{c}^{(n)} &=\frac{\tilde{F}_{c}^{(n)}}{\left\langle\tilde{F}_{c}^{(n)}\right\rangle_{c}} \\ Q_{p}^{(n)} &=\frac{\tilde{Q}_{p}^{(n)}}{\left\langle\tilde{Q}_{p}^{(n)}\right\rangle_{p}} 
\end{aligned}
$$


### References

Tacchella, Andrea, Matthieu Cristelli, Guido Caldarelli, Andrea Gabrielli, and Luciano Pietronero. 2012. “A New Metrics for Countries’ Fitness and Products’ Complexity.” *Scientific Reports* 2(1):723. doi: [10.1038/srep00723](https://doi.org/10.1038/srep00723).
