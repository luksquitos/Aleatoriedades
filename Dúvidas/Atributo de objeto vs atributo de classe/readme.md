# Atributo de objeto vs atributo de classe

Esse código surgiu nos ensinamentos iniciais do Tech With Tim e a principal dúvida era por que quant_amigos funcionava da forma esperada, mas não o list_amigos ?
Quando mandei minha dúvida para o Otavio Miranda, no dia 19/06/2022 eu havia compreendido algo errado. Que ```self.quant_amigos``` estava acessando a variável da classe, quando na verdade estava criando uma para o objeto instânciado. Isso é mostrado na 1ª Execução, que o obj var1 tem um atributo quant_amigos, mas não um list_amigos.

Outro problema que havia refletido muito era sobre todos poderem acessar a variável da classe e mudar seu valor. Mas acontece que isso também não acontece. 
Quando vamos fazer igual na 2ª execução, o programa procura se aquele objeto possui tal atributo, mas não encontra, posteriormente ele checa se a classe possui uma variável com aquele nome. 
Na terceira execução a variável taxa da classe manteve-se a mesma.


