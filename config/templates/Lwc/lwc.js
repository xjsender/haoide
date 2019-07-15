import { LightningElement, track } from 'lwc';

export default class Hello extends LightningElement {
    @track greeting = 'World';
}