//Arquitectura pantalla prueba1
//Declaración clase
class Marcadores{
	#id
	valor;
	#coordenadas_pantalla; //propiedad privada
	constructor(valor){
		this.valor= valor //aquí hay que ver como meterle los datos
//Clase hija
class Temperaturas extends Marcadores {
}
	
	
}
//creamos los objetos
int velocidad = new Marcadores();
int temprueda1 = new Temperaturas();
int temprueda2 = new Temperaturas();
int temprueda3 = new Temperaturas();
int temprueda4 = new Temperaturas();
int acelerador = new Marcadores();
int freno = new Marcadores();
int motor = new Marcadores();
int inversor = new Marcadores();
int baterias = new Marcadores();



// .insertAdjacentText(pos, text) nos permite insertar el texto text en la posición pos
// .remove () nos elimina los nodos en HTML
// para crear la animación mientras se inicia la rasperry 
// https://lenguajecss.com/css/animaciones/animaciones/ 
// .alert() para lanzar mensaje de error