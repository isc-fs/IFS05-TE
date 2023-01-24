class Marcador {
  private:
    float valor;
    int Id;

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