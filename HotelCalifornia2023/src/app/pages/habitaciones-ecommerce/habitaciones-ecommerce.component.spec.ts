import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HabitacionesEcommerceComponent } from './habitaciones-ecommerce.component';

describe('HabitacionesEcommerceComponent', () => {
  let component: HabitacionesEcommerceComponent;
  let fixture: ComponentFixture<HabitacionesEcommerceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HabitacionesEcommerceComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HabitacionesEcommerceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
