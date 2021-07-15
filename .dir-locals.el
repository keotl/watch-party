;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil . ((create-lockfiles . nil)
	 (eval . (with-eval-after-load 'treemacs
		   (defun treemacs-custom-filter
		       (file _)
		     (or
		      (s-ends-with\? "__pycache__" file)
		      (s-ends-with\? ".idea" file)))
		   (push #'treemacs-custom-filter treemacs-ignored-file-predicates))))))
