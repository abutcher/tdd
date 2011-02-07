
(let (files)
  (defun make  (&optional verbosep &rest new )
    (labels ((load1 (f) (format t "~a " f) (load f))
             (loads-shh (fs) (handler-bind 
                                 ((style-warning #'muffle-warning))
                               (mapcar #'load1 fs))))
      (format t "~&;")
      (if new (setf files new))
      (if verbosep 
          (mapcar #'load1 files)
          (loads-shh files))
      (format t "~&LITHP ITH LITHTENING~%")
      t)))


(make nil
      "tricks.lisp"
      ;"myfile.lisp"
      )


