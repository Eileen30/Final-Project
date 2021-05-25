import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreditcarddetailsComponent } from './creditcarddetails.component';

describe('CreditcarddetailsComponent', () => {
  let component: CreditcarddetailsComponent;
  let fixture: ComponentFixture<CreditcarddetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreditcarddetailsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreditcarddetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
