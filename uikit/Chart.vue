<template>
    <div class="grid p-fluid">
        <div class="col-12">
            <div class="card">
                <h5>Api de datos históricos del mercado de valores de Lyon, Francia</h5>
                <Chart type="line" :data="chartData" :options="options" class="h-30rem"></Chart>
            </div>

        </div>
        <div class="grid">
            <div class="col-12">
                <div class="card">
                    <h5>Cambio porcentual por dia de acciones AAPL (2017-01-05 / 2017-02-05)</h5>
                    <DataTable v-bind="value" :value="aapl" showGridlines paginator :rows="3"
                        :rowsPerPageOptions="[3, 10, 15, 24]" tableStyle="min-width: 50rem">
                        <Column field="date" header="Fecha"></Column>
                        <Column field="open" header="Valor Apertura"></Column>
                        <Column field="close" header="Valor Cierre"></Column>
                    </DataTable>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";
import { defineComponent } from 'vue';

export default defineComponent({
    data() {
        return {
            aapl: [],
            opciones: [],
            datos: [],
            chartData: {
                labels: [],
                datasets: [
                    {
                        label: 'Cambio porcentual trimestral',
                        data: [],
                        fill: false,
                        backgroundColor: '#2f4860',
                        borderColor: '#2f4860',
                        tension: .4
                    }
                ]
            },
            options: {
                responsive: true
            }
        };

    },
    async mounted() {
        axios.get("https://eodhistoricaldata.com/api/eod/MCD.US?from=2017-01-05&to=2017-02-05&period=d&fmt=json&api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX", {

        }).then((response) => {
            this.aapl = response.data;
            for (var i = 0; i < this.aapl.length; i++) {
                var counter = this.aapl[i];
                this.opciones.push(counter.date),
                this.datos.push(counter.close)
            }
            this.chartData.labels = this.opciones;
            this.chartData.datasets[0].data = this.datos;

        }).catch((error) => {
            console.log(error);
        });
    }
});
</script>
