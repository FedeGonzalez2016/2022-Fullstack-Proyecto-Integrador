import { TestBed } from '@angular/core/testing';

import { ConsultaService } from './consulta.service';

describe('ConsultaService', () => {
  let service: ConsultaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ConsultaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
