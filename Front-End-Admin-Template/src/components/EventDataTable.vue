
<template>
    <div class="card p-fluid">
        <!-- @filter="onFilter($event)" filterDisplay="row" -->
        <DataTable 
            :value="customers" 
            lazy 
            paginator 
            :first="first" 
            :rows="10" 
            v-model:filters="filters" ref="dt"
            dataKey="id" 
            :totalRecords="totalRecords" 
            :loading="loading" 
            @page="onPage($event)" 
            @sort="onSort($event)"
            :globalFilterFields="['name', 'country.name', 'company', 'representative.name']"
            v-model:selection="selectedCustomers" 
            :selectAll="selectAll" 
            @select-all-change="onSelectAllChange"
            @row-select="onRowSelect" 
            @row-unselect="onRowUnselect" 
            tableStyle="min-width: 75rem">
            
            <Column selectionMode="multiple" headerStyle="width: 3rem"></Column>
            <Column field="id" header="ID" filterMatchMode="startsWith" sortable>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search" />
                </template>
            </Column>
            <Column field="created_by.full_name" header="Full name" filterMatchMode="contains" sortable>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search" />
                </template>
            </Column>
            <Column field="created_by.profile" header="Profile" filterMatchMode="contains" sortable>
                <template #body="{ data }">
                    <div class="flex items-center">
                        <div class="flex-shrink-0 w-10 h-10"><img class="w-10 h-10 rounded-full"
                                src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&amp;auto=format&amp;fit=facearea&amp;facepad=2&amp;w=256&amp;h=256&amp;q=80"
                                alt=""></div>
                        <div class="ml-4">
                            <div class="text-sm font-medium leading-5 text-gray-900">{{ data.created_by.full_name }}</div>
                            <div class="text-sm leading-5 text-gray-500">{{ data.created_by.email }}</div>
                        </div>
                    </div>
                </template>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search" />
                </template>
            </Column>
            <Column field="status" header="Status" sortable>
                <template #body="{ data }">
                    <Badge value="{{ data.status }}" :severity="data.status == 'Open' ? 'success': 'warning'">{{ data.status }}</Badge>
                </template>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search" />
                </template>
            </Column>
            <Column field="mode" header="Mode" sortable>
                <template #body="{ data }">
                    <Badge value="{{ data.mode }}" :severity="data.mode == 'Online' ? 'success': 'warning'">{{ data.mode }}</Badge>
                </template>
                <template #filter="{ filterModel, filterCallback }">
                    <InputText type="text" v-model="filterModel.value" @keydown.enter="filterCallback()"
                        class="p-column-filter" placeholder="Search" />
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import server from '../server/index'


onMounted(() => {
    loading.value = true;

    lazyParams.value = {
        first: 0,
        rows: 10,
        sortField: null,
        sortOrder: null,
        filters: filters.value
    };

    loadLazyData();
});

const dt = ref();
const loading = ref(false);
const totalRecords = ref(0);
const customers = ref();
const selectedCustomers = ref();
const selectAll = ref(false);
const first = ref(0);
const filters = ref({
    'id': { value: '', matchMode: 'contains' },
    'title': { value: '', matchMode: 'contains' },
    'status': { value: '', matchMode: 'contains' },
    'created_by.full_name': { value: '', matchMode: 'contains' },
    'created_by.profile': { value: '', matchMode: 'contains' },
});
const lazyParams = ref({});
const columns = ref([
    { field: 'id', header: 'ID' },
    { field: 'title', header: 'Title' },
    { field: 'created_by.full_name', header: 'Name' },
    { field: 'created_by.profile', header: 'Profile' },
    { field: 'status', header: 'Status' }
]);

const loadLazyData = async (event) => {
    loading.value = true;
    lazyParams.value = { ...lazyParams.value, first: event?.first || first.value };
    console.log(lazyParams.value);
    const { data } = await server().get('event/');
    customers.value = data.data
    totalRecords.value = 20;
    loading.value = false;
};
const onPage = (event) => {
    console.log(event);
    lazyParams.value = event;
    loadLazyData(event);
};
const onSort = (event) => {
    lazyParams.value = event;
    loadLazyData(event);
};
const onFilter = (event) => {
    lazyParams.value.filters = filters.value;
    loadLazyData(event);
};
const onSelectAllChange = (event) => {
    selectAll.value = event.checked;

    if (selectAll) {
        CustomerService.getCustomers().then(data => {
            selectAll.value = true;
            selectedCustomers.value = data.customers;
        });
    }
    else {
        selectAll.value = false;
        selectedCustomers.value = [];
    }
};
const onRowSelect = () => {
    selectAll.value = selectedCustomers.value.length === totalRecords.value;
};
const onRowUnselect = () => {
    selectAll.value = false;
};

</script>
