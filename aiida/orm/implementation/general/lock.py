# -*- coding: utf-8 -*-

__copyright__ = u"Copyright (c), This file is part of the AiiDA platform. For further information please visit http://www.aiida.net/. All rights reserved."
__license__ = "MIT license, see LICENSE.txt file."
__version__ = "0.7.1"
__authors__ = "The AiiDA team."


class AbstractLockManager(object):
    """
    Management class to generate in a db-safe way locks.

    The class handles the generation of lock through the creation of database
    records with unique ``key`` fields using transaction-safe methods.
    """

    def aquire(self, key, timeout=3600, owner="None"):

        """
        The class tries to generate a new DbLock object with a key, unique in the model. If
        the creation goes good the Lock is generated and returned, if not an error is raised.
        :param key: the unique lock key, a string
        :param timeout: how long the
        :return: a Lock object
        :raise: InternalError: if there is an expired lock with the same input key
        :raise: LockPresent: if there is a Lock already present with the same key
        """

        raise NotImplementedError

    def clear_all(self):
        """
        Clears all the Locks, no matter if expired or not, useful for the bootstrap
        """
        raise NotImplementedError


class AbstractLock(object):
    """
    ORM class to handle the DbLock objects.

    Handles the release of the Lock, offers utility functions to test if a Lock
    is expired or still valid and to get the lock key.
    """

    def __init__(self, dblock):

        """
        Initialize the Lock object with a DbLock.
        :param dblock: a DbLock object generated by the LockManager
        """

        self.dblock = dblock

    def release(self, owner="None"):
        """
        Releases the lock deleting the DbLock from the database.
        :param owner: a string with the Lock's owner name
        :raise: ModificationNotAllowed: if the input owner is not the lock owner
        :raise: InternalError: if something goes bad with the database
        """

        raise NotImplementedError

    @property
    def isexpired(self):
        """
        Test whether a lock is expired or still valid
        """

        raise NotImplementedError

    @property
    def key(self):
        """
        Get the DbLock key
        :return: string with the lock key
        """
        raise NotImplementedError
