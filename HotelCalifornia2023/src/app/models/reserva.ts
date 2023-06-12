export class Reserva {
  constructor(
    public tipo:string,
    public descripcion:string,
    public servicios:Array<any>,
    public disponible:boolean,
    public precio:number
    ){}
}
