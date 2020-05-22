# Drowsiness-detection 🤖📷⚠️

O Projeto é sobre reconhecimento facial, se a pessoa está com sono ou não.

Você também pode ler este arquivo traduzido em
 - [English](../README.md)

***

O projeto tem como objetivo prover uma ferramenta de auxílio para motoristas, para os quais trabalham um longo tempo dirigindo, notificando caso esteja com sono ou não

A implementação do algoritimo teve como base no conteudo do articlo ["Real-Time Eye Blink Detection"](http://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf), onde aborda como detectar pontos de referencia em uma face humana e como mappear a posição dos olhos na face. Com estas informações, o algoritmo pode aplicar uma inteligência para detectar caso a pessoa esteja sonolenta.

Aqui é um exemplo...

![example](./example.gif)

# Requerimentos

- Python 3.3+

# 📚 Bibliotecas

* [dlib](http://dlib.net/python/index.html) - Para detectar as faces.
* [imutils](https://github.com/jrosebr1/imutils) - Para manipular operações e funções com openCV 
* [numpy](https://numpy.org/) - Prove um pacote para facilitar a manipulação de dados. 
* [scipy](https://www.scipy.org/) - Biblioteca usada para computação cientifica (Usada para calculos).

# ⚙ Como configurar?

``` bash
> python -m venv venv
> pip install -r requirements.txt
> source venv/bin/activate
```

# 🚀 Como usar?

É simples...

``` bash
> python detector.py
```

# 🔗 Referências

* [Distancia euclidiana](https://en.wikipedia.org/wiki/Euclidean_distance)
* [Reconhecimento de face](http://krasserm.github.io/2018/02/07/deep-face-recognition/)
* [Pontos de referencia da face](https://medium.com/@aanilkayy/extract-eyes-in-face-i%CC%87mages-with-dlib-and-face-landmark-points-c45ef480c1)