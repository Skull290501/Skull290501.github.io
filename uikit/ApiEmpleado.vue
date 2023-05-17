<template>
    <div class="grid">
        <div class="col-12 md:col-6">
            <div class="card">
                <h5>Consumir API REST Empleado</h5>
                <div class="p-fluid formgrid grid">
                    <div class="field col-12">
                        <label for="nombre">Nombre:</label>
                        <InputText id="nombre" type="text" :value="empleado.employee_name" readonly />
                    </div>
                    <div class="field col-12">
                        <label for="salario">Salario:</label>
                        <InputText id="salario" type="text" :value="empleado.employee_salary" readonly />
                    </div>
                    <div class="field col-12">
                        <label for="edad">Edad:</label>
                        <InputText id="edad" type="text" :value="empleado.employee_age" readonly />
                        <br>
                    </div>
                    <div class="field col-12">
                        <label for="number-input">ID Empleado</label>
                        <InputNumber id="number-input" v-model="id_emp" />
                    </div>
                    <div class="field col-12">
                        <Button label="Consultar Datos" class="p-button-success mr-2 mb-2" icon="pi pi-search"
                            @click="Consultar()" v-tooltip="'Click al presionar'"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <Toast/>
    <div class="grid">
        <div class="col-12">
            <div class="card">
                <div>
                    <h2>Lista de empleados</h2>
                    <DataTable v-bind="value" :value="empleados" showGridlines paginator :rows="3"
                        :rowsPerPageOptions="[3, 10, 15, 24]" tableStyle="min-width: 50rem">
                        <Column field="employee_name" header="Nombre"></Column>
                        <Column field="employee_salary" header="Salario"></Column>
                        <Column field="employee_age" header="Edad"></Column>
                    </DataTable>
                </div>
            </div>
        </div>
    </div>

</template>
<script>
import axios from "axios";
import { defineComponent } from 'vue';
export default defineComponent ({
    data() {
        return {
            empleados: [],
            id_emp: null,
            message: "No has ingresado su ID del empleado",
            empleado: {}
        };

    },
    mounted() {
        axios.get("https://dummy.restapiexample.com/api/v1/employees", {
            headers: {
                'Access-Control-Allow-Origin': '*',
            }
        }).then((response) => {
            this.empleados = response.data.data;
        })
            .catch((error) => {
                console.log(error);
            });
    },

    methods: {
        Consultar() {

            if (this.id_emp === null) {
                this.$toast.add({severity:'error', summary: 'Error al buscar', detail: 'No has Ingresado su ID del empleado', life: 5000});

            } else {
                axios.get(`https://dummy.restapiexample.com/api/v1/employee/${this.id_emp}`, {
                    headers: {
                        'Access-Control-Allow-Origin': '*',
                    }
                }).
                    then((response) => {
                        this.empleado = response.data.data;
                    }).catch((error) => {
                        alert("Error: " + error.response.status + " " + error.response.statusText);
                        console.log(error);
                    });
            }


        }
    }
});
</script>