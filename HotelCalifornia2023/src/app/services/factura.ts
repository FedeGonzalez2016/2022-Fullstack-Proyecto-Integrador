export interface Factura{
    facturaId: Number,
    nroFactura: Number,
    hotelId: Number,
    clienteId: Number,
           
 } ;
 
 export interface detalle{
    detalleId:Number,
    facturaId: Number,
    reservaId: Number,
    descuento: Number,
    importe: Number,    
 }

 export interface detallePago{
    detallePagoId: Number,
    tipoPagoId:Number,
     porcentajePago: Number,
 }

 export interface tipoPago{
        detallePagoId: Number,
        tipo:string;
 }
