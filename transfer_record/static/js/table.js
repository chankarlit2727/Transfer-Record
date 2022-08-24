$(document).ready(function () {
            var table = $('#example').DataTable({
                stateSave: true,
                stateLoadParams: function( settings, data ) {
                    if (data.order) delete data.order;
                  },
                autoWidth: false,

                dom: '<"toolbar">Bfrtlip',
                language: {
                    search: "_INPUT_",
                    searchPlaceholder: "Search..."
                },
                buttons: [
                {
                    extend: 'colvis',
                    text:   '<i class="fa-solid fa-sliders"></i>',
                    postfixButtons: [
                        {
                            text: 'Reset Default',
                            action: function ( e, dt, node, config ) {
                                table.column( 0 ).visible( true );
                                table.column( 1 ).visible( true );
                                table.column( 2 ).visible( true );
                                table.column( 3 ).visible( true );
                                table.column( 4 ).visible( true );
                                table.column( 5 ).visible( true );
                                table.column( 6 ).visible( true );
                                table.column( 7 ).visible( true );
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
                columns: [
                    { data: 'progress', width: '6%', searchable: false, className: "status_icon",
                     render: function (data, type, row) {
                        if (row.progress === "0") {
                            return '<i class="fa-solid fa-circle-xmark"></i>';}
                        else {
                            return '<i class="fa-solid fa-circle-check"></i>';
                        }
                    }
                    },
                    { data: 'type', width: '2%', searchable: false,
                    render: function (data, type, row) {
                        if (row.type == "1026") {
                            return '<td>KDM</td>';}
                        if (row.type == "1027") {
                            return '<td>DCP</td>';}
                        if (row.type == "1028") {
                            return '<td>SPL</td>';}
                        if (row.type == "1029") {
                            return '<td>PACK</td>';}
                        if (row.type == "1030") {
                            return '<td>RAR</td>';}
                    }},
                    { data: 'annotation', width: '10%', className: 'noVis' },
                    { data: 'theatre', width: '5%' },
                    { data: 'datetime', width: '10%', searchable: false,
                     render: function (data, type, row, meta) {
                        return moment.utc(data).local().format('YYYY-MM-DDTHH:mm:ss');
                    }},
                    { data: 'status', width: '9%', searchable: false,
                     render: function (data, type, row) {
                        if (row.status == "-1") {
                            return '<td>PENDING</td>';}
                        if (row.status == "0") {
                            return '<td>QUEUED</td>';}
                        if (row.status == "1") {
                            return '<td>IN_PROGRESS</td>';}
                        if (row.status == "2") {
                            return '<td>IN_PROGRESS_POST</td>';}
                        if (row.status == "3") {
                            return '<td>PAUSED</td>';}
                        if (row.status == "4") {
                            return '<td>FINISHED</td>';}
                        if (row.status == "5") {
                            return '<td>CANCELED</td>';}
                        if (row.status == "6") {
                            return '<td>EXCEPTION</td>';}
                        else{
                            return '<td>ERROR</td>';}
                    }
                    },
                    { data: 'messages', width: '28%', searchable: false,
                    render: $.fn.dataTable.render.ellipsis(150, true)},
                    { data: 'null', width: '4%', searchable: false },
                ]

            });



            $('div.toolbar').html('<a class="nav-link dropdown-toggle " href="#" data-bs-toggle="dropdown"><i class="fa-solid fa-trash-can"></i></a>\
							<ul class="dropdown-menu">\
							<li><a class="dropdown-item" href="#">Clear All Task</a></li>\
							<li><a class="dropdown-item" href="#">Clear Finished Task</a></li>\
							<li><a class="dropdown-item" href="#">Clear Exception Task</a></li>\
							<li><a class="dropdown-item" href="#">Clear Queued Task</a></li>\
							<li><a class="dropdown-item" href="#">Clear Pending Task</a></li>\
							</ul>');



        });