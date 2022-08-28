var dTable = $('#example').DataTable({
    dom: '<"toolbar">Bfrtlip',
    "serverSide": true,
    "ajax": { "url": "/api/record/", "type": "GET"},
    columns: [
        { data: 'record_progress', width: '6%', searchable: false, className: "status_icon",
        render: function (data, type, row) {
            if (row.record_progress === 0) {
                return '<i class="fa-solid fa-circle-xmark"></i>';}
            else {
                return '<i class="fa-solid fa-circle-check"></i>';
            }
        }},
        { data: 'record_type', width: '2%', searchable: false,
        render: function (data, type, row) {
            if (row.record_type == 1026) {
                return '<td>KDM</td>';}
            if (row.record_type == 1027) {
                return '<td>DCP</td>';}
            if (row.record_type == 1028) {
                return '<td>SPL</td>';}
            if (row.record_type == 1029) {
                return '<td>PACK</td>';}
            if (row.record_type == 1030) {
                return '<td>RAR</td>';}
        }},
        { data: 'record_annotation', width: '10%', className: 'noVis' },
        { data: 'record_theatre', width: '7%' },
        { data: 'record_datetime', width: '10%', searchable: false,
         render: function (data, type, row, meta) {
            return moment.utc(data).local().format('YYYY-MM-DDTHH:mm:ss');
        }},
        { data: 'record_status', width: '9%', searchable: false,
         render: function (data, type, row) {
            if (row.record_status == -1) {
                return '<td>PENDING</td>';}
            if (row.record_status == 0) {
                return '<td>QUEUED</td>';}
            if (row.record_status == 1) {
                return '<td>IN_PROGRESS</td>';}
            if (row.record_status == 2) {
                return '<td>IN_PROGRESS_POST</td>';}
            if (row.record_status == 3) {
                return '<td>PAUSED</td>';}
            if (row.record_status == 4) {
                return '<td>FINISHED</td>';}
            if (row.record_status == 5) {
                return '<td>CANCELED</td>';}
            if (row.record_status == 6) {
                return '<td>EXCEPTION</td>';}
            else{
                return '<td>ERROR</td>';}
        }},
        { data: 'record_exception_messages', width: '28%', 'searchable': false,
        render: $.fn.dataTable.render.ellipsis(150, true) },
        {
            data: null,
            defaultContent: '<button type="button" data-bs-toggle="modal" data-bs-target="#confirm"><i class="fa-solid fa-trash-can"></i></button>',
            width: '4%', searchable: false

        },

    ],
    buttons: [
    {
        extend: 'colvis',
        text:   '<i class="fa-solid fa-sliders"></i>',
        postfixButtons: [
            {
                text: 'Reset Default',
                action: function ( e, dt, node, config ) {
                    dTable.columns( 0 ).visible( true );
                    dTable.column( 1 ).visible( true );
                    dTable.column( 2 ).visible( true );
                    dTable.column( 3 ).visible( true );
                    dTable.column( 4 ).visible( true );
                    dTable.column( 5 ).visible( true );
                    dTable.column( 6 ).visible( true );
                    dTable.column( 7 ).visible( true );
            }
            }
        ],
        buttons : [{
            extend: 'columnsToggle'
        }],
        },
        {
            extend: 'csvHtml5',
            text: '<i class="fas fa-file-export"></i>',
            title: 'Record Export',
            exportOptions: {
                columns: ':visible',
                trim: false,
                stripNewlines: false,
                decodeEntities: false,
            }
        }
    ],
    "lengthMenu": [[10, 25, 50, 100, 100000000], [10, 25, 50, 100, "All"]],
    order: [[1, 'asc']],
    language: {
                    search: "_INPUT_",
                    searchPlaceholder: "Search..."
                },
    responsive: false,
    deferRender: true,
    autoWidth: false,
    scrollY: 410,
    scrollCollapse: true,
    stateSave: true,
    stateLoadParams: function( settings, data ) {
        if (data.order) delete data.order;
    }
});

/* Dropdown Bar (Top Left Button)*/

$('div.toolbar').html('<a class="nav-link dropdown-toggle " href="#" data-bs-toggle="dropdown"><i class="fa-solid fa-trash-can"></i></a>\
                        <ul class="dropdown-menu">\
                        <li><a class="dropdown-item" href="#">Clear All Task</a></li>\
                        <li><a class="dropdown-item" href="#">Clear Finished Task</a></li>\
                        <li><a class="dropdown-item" href="#">Clear Exception Task</a></li>\
                        <li><a class="dropdown-item" href="#">Clear Queued Task</a></li>\
                        <li><a class="dropdown-item" href="#">Clear Pending Task</a></li>\
                        </ul>');

/* Delete Row Button */

let id = 0;

$('#example tbody').on('click', 'button', function () {
    let data = dTable.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-primary') {
        // DELETE button
        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['record_id'];
    console.log(data);

});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/api/delete/' + id,
        method: 'DELETE',
        success:(function (data, textStatus, xhr) {
            location.reload();
        }),
        error:(function (jqXHR, textStatus, errorMessage) {
            console.log(jqXHR)
        })
    })
});