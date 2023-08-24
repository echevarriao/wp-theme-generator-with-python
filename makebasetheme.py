import os as fileSystem
import sys
import io

class ThemeBuilder:
	def __init__(self):
		self.themeName = ""
		self.themeVersion = ""
		self.authorUrl = ""
		self.themeUrl = ""
		self.themeDir = ""
		self.themeSlug = ""
		self.themeAuthor = ""
		
	def gatherInformation(self):
		
		themeName = input("Enter theme name: ")
		themeDir = input("Enter theme directory: ")
		themeVersion = input("Enter your theme version: ")
		authorUrl = input("Enter the author's URL: ")
		themeUrl = input("Enter the theme URL: ")
		themeSlug = input("Enter the theme slug: ")
		themeAuthor = input("Enter the theme author's name: ")

		self.themeName = themeName
		self.themeDir = themeDir
		self.themeVersion = themeVersion
		self.authorUrl = authorUrl
		self.themeUrl = themeUrl
		self.themeSlug = themeSlug
		self.themeAuthor = themeAuthor
		
	def createDirectories(self):
		themeParentDir = None
		myDir = None
		newDir = None
		themeDirs = ["css", "js", "images", "inc", "customizer", "templates"]
		
		themeParentDir = self.themeDir
		
		fileSystem.makedirs(themeParentDir)

		for myDir in themeDirs:
			newDir = fileSystem.path.join(themeParentDir, myDir)
			fileSystem.mkdir(newDir)

			print("New directory: " + newDir)

	# end createDirectories

	def createFiles(self):
		
		postFormats = ["404", "archive", "image", "link", "audio", "single", "aside", "chat", "quote", "gallery", "status", "video"]
		nonPostFormats = ["content", "functions", "index", "header",  "footer"]
		
		data = None
		output = None;
		
		for data in postFormats:
			output = open(self.themeDir + "/" + data + ".php", "w")
			output.write("""<?php
/**
 * The template for displaying """ + data + """
 *
 * This is the template that displays all pages by default.
 * Please note that this is the WordPress construct of pages and that
 * other "pages" on your WordPress site will use a different template.
 *
 * @package WordPress
 * @subpackage """ + self.themeName + """
 * @since """ + self.themeName + """ 1.0
 */

get_header(); ?>

	<div id="primary" class="content-area">
		<main id="main" class="site-main">

		<?php
		// Start the loop.
		while ( have_posts() ) :
			the_post();""")
			output.write("""
						 
			// Include the page content template.
			get_template_part( 'content', '""" + data + """');

			// If comments are open or we have at least one comment, load up the comment template.
			if ( comments_open() || get_comments_number() ) :
				comments_template();
			endif;

			// End the loop.
		endwhile;
		?>

		</main><!-- .site-main -->
	</div><!-- .content-area -->

<?php get_footer(); ?>""")
			output.close()
			print("New file generated: "  + self.themeDir + "/" + data + ".php")
			
			output = open(self.themeDir + "/content-" + data + ".php", "w")
			output.write("""
<?php
/**
 * The template used for displaying """ + data +""" content
 *
 * @package WordPress
 * @subpackage """ + self.themeName + """
 * @since """ + self.themeName + """ 1.0
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>

	<header class="entry-header">
		<?php the_title( '<h1 class="entry-title">', '</h1>' ); ?>
	</header><!-- .entry-header -->

	<div class="entry-content">
		<?php the_content(); ?>
		<?php
			wp_link_pages(
				array(
					'before'      => '<div class="page-links"><span class="page-links-title">' . __( 'Pages:', '""" + self.themeSlug + """' ) . '</span>',
					'after'       => '</div>',
					'link_before' => '<span>',
					'link_after'  => '</span>',
					/* translators: Hidden accessibility text. */
					'pagelink'    => '<span class="screen-reader-text">' . __( 'Page', 'twentyfifteen' ) . ' </span>%',
					'separator'   => '<span class="screen-reader-text">, </span>',
				)
			);
			?>
	</div><!-- .entry-content -->

	<?php edit_post_link( __( 'Edit', '""" + self.themeSlug + """' ), '<footer class="entry-footer"><span class="edit-link">', '</span></footer><!-- .entry-footer -->' ); ?>

</article><!-- #post-<?php the_ID(); ?> -->""")
			output.close()
			print ("New file generated: " + self.themeDir + "/content-" + data + ".php")

	# end of createFiles
	
	def createStyleSheet(self):
		
		styles = ["style.css"]
		output = None
		
		for s in styles:
			output = open(self.themeDir + "/" + s, "w")
			
			output.write("""	/*
Theme Name: """ + self.themeName + """
Theme URI: """ + self.themeUrl + """
Author: """ + self.themeAuthor + """
Author URI: """ + self.authorUrl + """
Description: Our 2015 default theme is clean, blog-focused, and designed for clarity. Twenty Fifteen's simple, straightforward typography is readable on a wide variety of screen sizes, and suitable for multiple languages. We designed it using a mobile-first approach, meaning your content takes center-stage, regardless of whether your visitors arrive by smartphone, tablet, laptop, or desktop computer.
Version: """ + self.themeVersion + """
Requires at least: 6.0
Tested up to: 6.0
Requires PHP: 5.3.0
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Tags: blog, two-columns, left-sidebar, accessibility-ready, custom-background, custom-colors, custom-header, custom-logo, custom-menu, editor-style, featured-images, microformats, post-formats, rtl-language-support, sticky-post, threaded-comments, translation-ready, block-patterns
Text Domain: """ + self.themeSlug + """

This theme, like WordPress, is licensed under the GPL.
Use it to make something cool, have fun, and share what you've learned with others.

	*
	*/
						 
			""")
			output.close()
			
		# end of createStyleSheet
	
	
#end of methods and class
		
		
theme = ThemeBuilder()
theme.gatherInformation()
theme.createDirectories()
theme.createFiles()
theme.createStyleSheet()