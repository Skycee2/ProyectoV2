
function confirmar() {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Deleted!',
                'Your file has been deleted.',
                'success'
            )
        }
    })
}

$(document).ready(function () {
    $('.btn-aside').on('click', function () {
  
      $('.line-1').toggleClass('line-1-open');
      $('.line-2').toggleClass('line-2-open');
      $('.line-3').toggleClass('line-3-open');
      $('.sidebar').toggleClass('sidebar-open');

    });
  });