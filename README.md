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


<svg xmlns="http://www.w3.org/2000/svg" width="10.491ex" height="3.639ex" role="img" focusable="false" viewBox="0 -1224.4 4637.2 1608.6" style="vertical-align: -0.869ex;"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><g data-mml-node="math"><g data-mml-node="msubsup"><g data-mml-node="TeXAtom" data-mjx-texclass="ORD"><g data-mml-node="mover"><g data-mml-node="mi"><path data-c="51" d="M399 -80Q399 -47 400 -30T402 -11V-7L387 -11Q341 -22 303 -22Q208 -22 138 35T51 201Q50 209 50 244Q50 346 98 438T227 601Q351 704 476 704Q514 704 524 703Q621 689 680 617T740 435Q740 255 592 107Q529 47 461 16L444 8V3Q444 2 449 -24T470 -66T516 -82Q551 -82 583 -60T625 -3Q631 11 638 11Q647 11 649 2Q649 -6 639 -34T611 -100T557 -165T481 -194Q399 -194 399 -87V-80ZM636 468Q636 523 621 564T580 625T530 655T477 665Q429 665 379 640Q277 591 215 464T153 216Q153 110 207 59Q231 38 236 38V46Q236 86 269 120T347 155Q372 155 390 144T417 114T429 82T435 55L448 64Q512 108 557 185T619 334T636 468ZM314 18Q362 18 404 39L403 49Q399 104 366 115Q354 117 347 117Q344 117 341 117T337 118Q317 118 296 98T274 52Q274 18 314 18Z"></path></g><g data-mml-node="mo" transform="translate(228.8, 549)"><path data-c="7E" d="M179 251Q164 251 151 245T131 234T111 215L97 227L83 238Q83 239 95 253T121 283T142 304Q165 318 187 318T253 300T320 282Q335 282 348 288T368 299T388 318L402 306L416 295Q375 236 344 222Q330 215 313 215Q292 215 248 233T179 251Z"></path></g></g></g><g data-mml-node="TeXAtom" transform="translate(791, 694.1) scale(0.707)" data-mjx-texclass="ORD"><g data-mml-node="mo"><path data-c="28" d="M94 250Q94 319 104 381T127 488T164 576T202 643T244 695T277 729T302 750H315H319Q333 750 333 741Q333 738 316 720T275 667T226 581T184 443T167 250T184 58T225 -81T274 -167T316 -220T333 -241Q333 -250 318 -250H315H302L274 -226Q180 -141 137 -14T94 250Z"></path></g><g data-mml-node="mn" transform="translate(389, 0)"><path data-c="30" d="M96 585Q152 666 249 666Q297 666 345 640T423 548Q460 465 460 320Q460 165 417 83Q397 41 362 16T301 -15T250 -22Q224 -22 198 -16T137 16T82 83Q39 165 39 320Q39 494 96 585ZM321 597Q291 629 250 629Q208 629 178 597Q153 571 145 525T137 333Q137 175 145 125T181 46Q209 16 250 16Q290 16 318 46Q347 76 354 130T362 333Q362 478 354 524T321 597Z"></path></g><g data-mml-node="mo" transform="translate(889, 0)"><path data-c="29" d="M60 749L64 750Q69 750 74 750H86L114 726Q208 641 251 514T294 250Q294 182 284 119T261 12T224 -76T186 -143T145 -194T113 -227T90 -246Q87 -249 86 -250H74Q66 -250 63 -250T58 -247T55 -238Q56 -237 66 -225Q221 -64 221 250T66 725Q56 737 55 738Q55 746 60 749Z"></path></g></g><g data-mml-node="TeXAtom" transform="translate(791, -247) scale(0.707)" data-mjx-texclass="ORD"><g data-mml-node="mi"><path data-c="70" d="M23 287Q24 290 25 295T30 317T40 348T55 381T75 411T101 433T134 442Q209 442 230 378L240 387Q302 442 358 442Q423 442 460 395T497 281Q497 173 421 82T249 -10Q227 -10 210 -4Q199 1 187 11T168 28L161 36Q160 35 139 -51T118 -138Q118 -144 126 -145T163 -148H188Q194 -155 194 -157T191 -175Q188 -187 185 -190T172 -194Q170 -194 161 -194T127 -193T65 -192Q-5 -192 -24 -194H-32Q-39 -187 -39 -183Q-37 -156 -26 -148H-6Q28 -147 33 -136Q36 -130 94 103T155 350Q156 355 156 364Q156 405 131 405Q109 405 94 377T71 316T59 280Q57 278 43 278H29Q23 284 23 287ZM178 102Q200 26 252 26Q282 26 310 49T356 107Q374 141 392 215T411 325V331Q411 405 350 405Q339 405 328 402T306 393T286 380T269 365T254 350T243 336T235 326L232 322Q232 321 229 308T218 264T204 212Q178 106 178 102Z"></path></g></g></g><g data-mml-node="mo" transform="translate(2022.5, 0)"><path data-c="3D" d="M56 347Q56 360 70 367H707Q722 359 722 347Q722 336 708 328L390 327H72Q56 332 56 347ZM56 153Q56 168 72 173H708Q722 163 722 153Q722 140 707 133H70Q56 140 56 153Z"></path></g><g data-mml-node="mn" transform="translate(3078.2, 0)"><path data-c="31" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path></g><g data-mml-node="mi" transform="translate(3578.2, 0)"><path data-c="2200" d="M0 673Q0 684 7 689T20 694Q32 694 38 680T82 567L126 451H430L473 566Q483 593 494 622T512 668T519 685Q524 694 538 694Q556 692 556 674Q556 670 426 329T293 -15Q288 -22 278 -22T263 -15Q260 -11 131 328T0 673ZM414 410Q414 411 278 411T142 410L278 55L414 410Z"></path></g><g data-mml-node="mi" transform="translate(4134.2, 0)"><path data-c="70" d="M23 287Q24 290 25 295T30 317T40 348T55 381T75 411T101 433T134 442Q209 442 230 378L240 387Q302 442 358 442Q423 442 460 395T497 281Q497 173 421 82T249 -10Q227 -10 210 -4Q199 1 187 11T168 28L161 36Q160 35 139 -51T118 -138Q118 -144 126 -145T163 -148H188Q194 -155 194 -157T191 -175Q188 -187 185 -190T172 -194Q170 -194 161 -194T127 -193T65 -192Q-5 -192 -24 -194H-32Q-39 -187 -39 -183Q-37 -156 -26 -148H-6Q28 -147 33 -136Q36 -130 94 103T155 350Q156 355 156 364Q156 405 131 405Q109 405 94 377T71 316T59 280Q57 278 43 278H29Q23 284 23 287ZM178 102Q200 26 252 26Q282 26 310 49T356 107Q374 141 392 215T411 325V331Q411 405 350 405Q339 405 328 402T306 393T286 380T269 365T254 350T243 336T235 326L232 322Q232 321 229 308T218 264T204 212Q178 106 178 102Z"></path></g></g></g></svg>

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <msubsup>
    <mrow>
      <mover>
        <mi>Q</mi>
        <mo stretchy="false">~</mo>
      </mover>
    </mrow>
    <mrow>
      <mi>p</mi>
    </mrow>
    <mrow>
      <mo stretchy="false">(</mo>
      <mn>0</mn>
      <mo stretchy="false">)</mo>
    </mrow>
  </msubsup>
  <mo>=</mo>
  <mn>1</mn>
  <mi mathvariant="normal">∀</mi>
  <mi>p</mi>
</math>

### References

Tacchella, Andrea, Matthieu Cristelli, Guido Caldarelli, Andrea Gabrielli, and Luciano Pietronero. 2012. “A New Metrics for Countries’ Fitness and Products’ Complexity.” *Scientific Reports* 2(1):723. doi: [10.1038/srep00723](https://doi.org/10.1038/srep00723).
