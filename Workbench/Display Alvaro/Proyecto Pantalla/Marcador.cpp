class Marcador {
  private:
    float valor;
    int Id;
    
// lo que yo pienso que hay que hacer es con esta clase, 
// ir haciendo objetos para cada una de las cajas que pongamos en el display. 
// Habría que ver cómo hacemos para las barras de la aceleración, revoluciones y SoC

  public:
    Marcador(){
      valor = 0.0;
      Id = 00000000000000000000000000000000;
    }
    void setValor(float v){
      valor = v;
    }
    float getValor(){
      return valor;
    }

    void setId(int id){
      Id = id;
    }

    int getId(){
      return Id
    }
};